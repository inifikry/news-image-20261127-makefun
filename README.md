[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/inifikry/news-image-20261127-makefun/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/inifikry/news-image-20261127-makefun/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
# The World in One Day — Friday 27 November 2026

Front-page image summing up the world news of Friday 27 November 2026,
for the make.fun bounty `news-image-20261127`.

## How it works

`main.py` copies the pre-rendered image `entry.png` (1024x1024 PNG,
under 1 MiB) to `/output/entry.png`. No network is used at run time.
The image itself was drawn offline with Python + PIL by `draw_news.py`
(DejaVu fonts, all text rendered by PIL, no copied artwork).

## Stories in the image

1. **Middle East — Drone strike in Kuwait kills two Italians.**
   Italy and Kuwait blame Iran for the attack on an air-defence station;
   Tehran denies any role. The two dead were Rheinmetall technicians.
   Sources: Reuters, The New York Times, BBC.
2. **United States — Storm stops the Macy's parade.**
   First weather postponement in the parade's 100 years; 850,000+ homes
   lost power on Thanksgiving. Source: Daily Fox News / FlightAware /
   PowerOutage.us, reported 27 Nov 2026 00:17 UTC.
3. **New Zealand — Final vote keeps coalition in power.**
   Slim majority confirmed: 67 of 131 seats after the final count.
   Source: Newstalk ZB, Morning Edition 27 November 2026.
4. **Sport / Chess — Chess title deadlocked.**
   Gukesh and Sindarov draw a marathon Game 3 of the World Championship;
   all square after three games. Source: India Today / The Hindu,
   reported 27 Nov 2026.
5. **Argentina — Milei wins in Congress.**
   Senate suspends the 2027 primaries; the central bank is barred from
   funding the state. Sources: Reuters, The Insight International,
   27 Nov 2026.
6. **United Kingdom — UK net migration falls to 77,000.**
   Lowest since 1997 outside the pandemic, the ONS says — down from
   204,000 a year earlier. Sources: ONS, Reuters, BBC.

## Verify

```
python3 main.py
sha256sum /output/entry.png
```
