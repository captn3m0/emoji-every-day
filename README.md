---
layout: default
title: Emoji Every Day
permalink: /about/
---

An emoji character for (almost) every day.

Data in [`_data/emoji.yaml`](https://github.com/captn3m0/emoji-every-day/blob/main/_data/emoji.yml). Made for India, but can be extended to other countries.

Includes:

- Informally observed holidays
- [List of International Days and Weeks observed by United Nations][undays]

## Format

The `emoji.yaml` file contains a dictionary with keys in either `YYYY-MM-DD` or `MM-DD` format,
depending on whether the holiday is fixed or floating.

Each date contains a list of events, each event consisting of the following keys:

- `emoji`: A short single-grapheme representation of the event. Almost always an emoji, but can ocassionaly be a different unicode codepoint.
- `day_name`: Human-readable name of the event, in english
- `type`: UN/informal/2-letter ISO country code
- `link`: A valid web URL. Optional.

## Emoji Choices

There aren't enough emojis to represent a lot of things, so this is best-effort. If you have an improvement, please file a PR.
In some cases, due to unicode standard updates taking time to rollout, the emoji may show as multiple characters, such
as the [Refugee Flag](https://emojipedia.org/refugee-nation-flag) (🏳‍🟧‍⬛‍🟧), which shows up as 4 characters almost everywhere, since
the proposal isn't accepted yet.

## License

Licensed under the [MIT License](https://nemo.mit-license.org/). 
See LICENSE file for details.

## Why

Think of this as a poor man's Google Doodle for any website, where you might have daily refreshes. I'm currently using it for [news.tatooine.club](https://news.tatooine.club),
where I wanted to put a 🎄 next to the date for Christmas, but extended it to this project. See [Origin Post](https://tatooine.club/@nemo/111647981554186397) for more details.

[undays]: https://www.un.org/en/observances/list-days-weeks