# Contributing Capta to DILMS

If you are contributing capta to DILMS, please follow these guidelines as closely as possible.
If you encounter a circumstance that isn't covered by the guidelines, please get in touch and ask for guidance.
That way we can be proactive about any changes that need to be made to other parts of the project.

## General Guidelines

Whenever you start work on a new capta-related item (editing existing entries, adding new entries, etc.), you should fork a new branch from `develop` called `feature/capta/[descriptor]` and do your work there.
For example, if I wanted to suggest changes to DILMS's entries for the Mellon Chansonnier I would fork a new branch called `feature/capta/edit-mellon`, and if I wanted to add entries to DILMS's tables to account for the manuscript Turin J.II.9 I would fork a new branch called `feature/capta/add-turin-J-II-9`.
Branch names are ultimately up to the discretion of the contributor, but should generally be short, legible, and begin with a descriptive verb (edit, add, delete, etc.).
Branches should be confined to discrete and isolable changes.
For example, if you're adding a newly discovered manuscript and its contents to DILMS, but that manuscript's appearance has also impacted the dating of several other manuscripts already in DILMS, then those ensuing chronological edits should be handled in a separate branch from the new additions.

Additional formatting guidelines coming soon.

## Table-Specific Guidelines

### `sources`
Coming soon.

### `source_layers`
Coming soon.

### `inscriptions`
Coming soon.

### `songs`
Coming soon.

## Submitting Your Work

When your work is complete and ready to be integrated into DILMS, the first thing you should do is rebase your work on the latest version of `develop` (do this by running `git rebase develop` in the command line while in your `feature/` branch) and resolve any merge conflicts.
Then, open a pull request to merge your branch into `develop`.
Please use the [capta PR template](../.github/PULL_REQUEST_TEMPLATE/capta_template.md) to structure your request&mdash;this should be an option you can select on GitHub.
Be sure to complete the checklist (except for the final item) and add the requested information before formally opening the request.
Your request must be reviewed by *at least two people* before it can be completed.
After you have incorporated your reviewers' feedback, the request has been approved, and the final item in the checklist has been completed, you may merge your branch into `develop`.
Note that you will not see your work reflected in the public version of DILMS until the next official release.
