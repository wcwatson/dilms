# DILMS | Digital Index of Late Medieval Song

The Digital Index of Late Medieval Song is an interactive database that aims to describe every inscription of vernacular polyphony from 15th-century Europe.
Its original, "pre-pre-release" version was constructed as part of my dissertation project, ["Circulating Song from the Century before Print (2020)."][1]
The current public release may, of course, be found at [dilms.org][2].
I am preparing an article that discusses the curation of DILMS through the lens of critical data studies; additional details will be posted here as they become available.


## Project Structure

### `capta/`
This directory contains the source capta for DILMS.
If you're making additions to the "content" of the database (adding inscriptions, manuscripts, etc.), this is where you'll be doing most of your work.

### `dilms/`
This directory contains the Flask Web app that powers [the current version of DILMS][2].

#### `static/`
This directory contains static images, style configurations, and other "immutable" files.

#### `templates/`
This directory contains HTML templates that DILMS renders dynamically based on user input.

#### `sql.py`
This module helps manage DILMS's SQL functionality, from sanitizing input to formatting results.

#### `routes.py`
This module defines the app's interactive functionality.

### `environment.yml`
This YAML file defines a virtual environment that needs to be active to run DILMS.
See below for further details.


## Get Involved

If you are interested in contributing to DILMS, please feel free to [get in touch](mailto:admin@dilms.org) and we'll talk about what you might work on!

### Getting Started
Once you're ready to start working on the project, clone this repo on your local machine and make a new virtual environment called `dilms` using the configurations in `environment.yml`.
You'll use that virtual environment for all DILMS-related work.
If you've done this kind of work before, then you know what the preceding instructions mean and you should be ready to go.
If not, don't panic!
Follow the more detailed directions below (they assume that you're working on a Mac).

First, make sure you have [Anaconda][3] installed on your machine.
Anaconda gives us a handy way to manage our virtual environments, which practically speaking means that it ensures we're working with the right versions of all of the packages we need, even if we decide to use a different version for another project.
Once you've installed Anaconda, open a Terminal window in the directory where you want to store your local copy of DILMS (e.g., mine is in `/Desktop/DILMS/`).
If you're new to the command line and aren't sure how to do that, spend some time with [this helpful blog post][4] and proceed when you feel comfortable `cd`ing and `ls`ing your way around.
Once you've opened a Terminal window in the right place, run the following commands.
```bash
>> git clone https://github.com/wcwatson/dilms.git

>> cd dilms

>> conda env create -f environment.yml
```
The first command will clone the repo to the location you've specified on your local machine.
The second will take you into the repo's root directory.
The third will create a new virtual environment called `dilms` that has all of the packages you will need to work on this project.
If at any point you need to activate this environment, just run `conda activate dilms` in a Terminal window.
When you're done, leave the environment by running `conda deactivate`, and you can go about your other business.

### Workflow
DILMS follows [the Gitflow workflow][5] in spirit, although I don't make use of the git-flow extension library.
Practically, this means that all work should be based off of the `develop` branch; the `master` branch is used only for official releases.
Whenever you start work on a new feature, create a new branch off of `develop` called `feature/[feature-name]`.
If you are working on a capta-related "feature" (e.g., adding a new manuscript or editing inscriptions), your feature branch should be called `feature/capta/[descriptor]`.
When your work on that feature is finished and ready for review, open a pull request to merge your feature branch into `develop`.
**NEVER** commit changes directly to `develop`.

If you have limited experience with `git`, I recommend checking out a few of [the resources and tutorials available on Github][6].
I recommend using the command line as much as possible to perform `git` operations, since it offers a lot of flexibility.
However, there are desktop `git` clients available if the command line just isn't your thing&mdash;[GitHub Desktop](https://desktop.github.com/) is a good one.
I also recommend acquainting yourself with [best practices for `commit` messages][7].

### Contributing
If you are making changes to the capta made available through DILMS (i.e., making changes to the `capta/` directory), please follow the guidelines in [capta/CONTRIBUTING.md](capta/CONTRIBUTING.md) and use [capta_template.md](.github/PULL_REQUEST_TEMPLATE/capta_template.md) for your pull requests.
If you are contributing to the functionality of the app (i.e., making changes to the `flask/` directory), please follow the guidelines in [flask/CONTRIBUTING.md](flask/CONTRIBUTING.md) and use [flask_template.md](.github/PULL_REQUEST_TEMPLATE/flask_template.md) for your pull requests.

[1]: <https://www.researchgate.net/publication/340849806_Circulating_Song_from_the_Century_before_Print>
[2]: <http://www.dilms.org>
[3]: <https://www.anaconda.com/>
[4]: <https://medium.com/@grace.m.nolan/terminal-for-beginners-e492ba10902a>
[5]: <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>
[6]: <https://try.github.io/>
[7]: <https://chris.beams.io/posts/git-commit/>
