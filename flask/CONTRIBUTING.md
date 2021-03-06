# Contributing to the DILMS App

When you start work on a new feature, fork a branch from `develop` with a name of the format `feature/[descriptor]` and do your work there.
Branch names are ultimately up to the discretion of the developer, but should be short and intuitive.
For instance, if I were working on a new webpage that collated links to useful external resources, I might fork a branch called `feature/add-resource-pg`.
If later, a while after that page had been released, I wanted to add some search functionality to that page, I might fork a new branch called `feature/search-resources` to do that work.

When your work is complete and ready to be integrated into DILMS, open a pull request to merge your branch into `develop`.
**DO NOT** rebase your branch on `develop`.
Rebasing is appropriate for capta-related work because it helps prevent contributors from overwriting each others' commits.
However, for work on the app itself we want a faithful historical record, even if that means a bunch of messy merges.
Please use the [flask PR template](../.github/PULL_REQUEST_TEMPLATE/flask_template.md) to structure your request&mdash;this should be an option you can select on GitHub.
Be sure to complete the checklist and add the requested information before formally opening the request.
Your request must be reviewed by *at least two people* before it can be completed.
After you have incorporated your reviewers' feedback and the request has been approved, you may merge your branch into `develop`.
Note that you will not see your work reflected in the public version of DILMS until the next official release.

## Style Guidelines
For Python, try to follow [the Google style guide](https://google.github.io/styleguide/pyguide.html), with the following exceptions.
- Partial imports (e.g., `from dilms.sql import inspect_and_execute`) are allowed, so long as their origin is reasonably clear.

Guidelines for HTML, SQL, and other relevant languages coming soon.
 