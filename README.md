# Hop Along Books

Color by number books for kids ages 3-5. Site source for https://hopalongbooks.github.io

Edit `_build.py` and run `python3 _build.py` to regenerate the pages.

## Home page script
`assets/home.js` is a static file (not generated). It runs the living page, the book finder quiz, the level ladder and the try-it colorer on the home page. Book data reaches it through `window.HAB`, which `_build.py` writes from `BOOKS`, so prices, links and status stay in one place.
Character stickers (`img/st_*.png`) are cut out of the answer pictures; `img/book*_cover_sm.jpg` are smaller covers for the home hero.
