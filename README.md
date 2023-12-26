# Emoji Every Day

An emoji character for (almost) every day.

Data in emoji.yaml. Made for India, but can be extended to other countries.

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

[undays]: https://www.un.org/en/observances/list-days-weeks