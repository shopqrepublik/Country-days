# Schengen Family Planner

Private family PWA for Schengen 90/180 planning.

- GitHub Pages hosts the static PWA.
- Supabase stores one shared family state.
- Access is protected by the family PIN; the PIN itself is not committed to GitHub.
- LocalStorage keeps an offline copy; JSON backup/restore remains available.
- Open devices pull newer shared data on unlock, focus/visibility, and every 15 seconds while visible.
