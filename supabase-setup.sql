-- Run once in Supabase SQL Editor.
-- IMPORTANT: replace YOUR_FAMILY_PIN below before running.

create extension if not exists pgcrypto;

create table if not exists public.family_sync (
  id text primary key,
  pin_hash text not null,
  state jsonb,
  updated_at timestamptz not null default now()
);

alter table public.family_sync enable row level security;
revoke all on table public.family_sync from anon, authenticated;

insert into public.family_sync(id,pin_hash,state)
values ('family', crypt('YOUR_FAMILY_PIN', gen_salt('bf')), null)
on conflict (id) do update set pin_hash=excluded.pin_hash;

create or replace function public.family_state_get(p_pin text)
returns jsonb
language plpgsql
security definer
set search_path = public, pg_temp
as $$
declare r public.family_sync%rowtype;
begin
  select * into r from public.family_sync where id='family';
  if r.id is null or crypt(p_pin,r.pin_hash) <> r.pin_hash then
    raise exception 'Invalid PIN' using errcode='28000';
  end if;
  return jsonb_build_object('state',r.state,'updated_at',r.updated_at);
end;
$$;

create or replace function public.family_state_save(p_pin text,p_state jsonb)
returns jsonb
language plpgsql
security definer
set search_path = public, pg_temp
as $$
declare r public.family_sync%rowtype;
begin
  select * into r from public.family_sync where id='family' for update;
  if r.id is null or crypt(p_pin,r.pin_hash) <> r.pin_hash then
    raise exception 'Invalid PIN' using errcode='28000';
  end if;
  update public.family_sync set state=p_state,updated_at=now() where id='family' returning * into r;
  return jsonb_build_object('updated_at',r.updated_at);
end;
$$;

revoke all on function public.family_state_get(text) from public;
revoke all on function public.family_state_save(text,jsonb) from public;
grant execute on function public.family_state_get(text) to anon, authenticated;
grant execute on function public.family_state_save(text,jsonb) to anon, authenticated;
