# How to contribute to <PROJECT NAME>

Everyone is welcome to contribute, and we value everybody's contribution.

There are many ways to contribute to <PROJECT NAME>, with the most common ones being contribution of code or documentation to the project. 
Improving the documentation is no less important than improving the library itself. If you find a typo in the documentation, or have made improvements, do not hesitate to send an email to the mailing list or preferably submit a GitHub pull request. 
Documentation can be found under the `doc/` directory.

Another way to contribute is to report issues you're facing, and give a "thumbs up" on issues that others reported and that are relevant to you. 
It also helps us if you spread the word: reference the project from your blog and articles, link to it from your website, or simply star it in GitHub to say "I use it".

Whichever way you choose to contribute, please be mindful to respect our [code of conduct]().

## Ways to contribute

* Fixing outstanding issues with the existing code.
* Contributing to the documentation.
* Submitting issues related to bugs or desired new features.

## Quick links

* Submitting a bug report or feature request

* Contributing code

## Submitting a bug report or feature request

Do your best to follow these guidelines when submitting an issue or a feature request.

### Did you find a bug?

Thank you for reporting an issue!

We use GitHub issues to track all bugs and feature requests; feel free to open an issue if you have found a bug or wish to see a feature implemented.

In case you experience issues using this package, do not hesitate to submit a ticket to the Bug Tracker. You are also welcome to post feature requests or pull requests.

First, we would really appreciate it if you could make sure the bug was not already reported (use the search bar on Github under Issues).

Did not find it? In order to act quickly on it, please follow these steps:

* Include your OS type and version, the versions of Python, or other libraries.
* A short, self-contained, code snippet that allows us to reproduce the bug in less than 30s.
* Provide the full traceback if an exception is raised.
* If you are submitting a bug report, we strongly encourage you to follow the guidelines in [How to make a good bug report]().

#### How to make a good bug report

When you submit an issue to Github, please do your best to follow these guidelines! 
This will make it a lot easier to provide you with good feedback:

* The ideal bug report contains a short reproducible code snippet, this way anyone can try to reproduce the bug easily (see this for more details). 
If your snippet is longer than around 50 lines, please link to a gist or a github repo.

* If not feasible to include a reproducible snippet, please be specific about what estimators and/or functions are involved and the shape of the data.

* If an exception is raised, please provide the full traceback.

* Please include your operating system type and version number, as well as your Python, and <OTHER IMPORTANT PACKAGES> versions.

* Please ensure all code snippets and error messages are formatted in appropriate code blocks. 
See [Creating and highlighting code blocks](https://help.github.com/articles/creating-and-highlighting-code-blocks) for more details.



### Do you want a new feature?

A world-class feature request addresses the following points:

1. Motivation first:
* Is it related to a problem/frustration with the library? If so, please explain why. Providing a code snippet that demonstrates the problem is best.
* Is it related to something you would need for a project? We'd love to hear about it!
* Is it something you worked on and think could benefit the community? Awesome! Tell us what problem it solved for you.

2. Write a full paragraph describing the feature;
3. Provide a code snippet that demonstrates its future use;
4. In case this is related to a paper, please attach a link;
5. Attach any additional information (drawings, screenshots, etc.) you think may help.

If your issue is well written we're already 80% of the way there by the time you post it.

We have added templates to guide you in the process of adding a new example script for training or testing the models in the library. You can find them in the [templates folder]().


## Contributing code

**Note:** *To avoid duplicating work, it is highly advised that you search through the issue tracker and the PR list. If in doubt about duplicated work, or if you want to work on a non-trivial feature, it’s recommended to first open an issue in the issue tracker to get some feedbacks from core developers.
One easy way to find an issue to work on is by applying the “help wanted” label in your search. This lists all the issues that have been unclaimed so far. In order to claim an issue for yourself, please comment exactly take on it for the CI to automatically assign the issue to you.*

### How to contribute

The preferred way to contribute to <PROJECT NAME> is to fork the main repository on GitHub, then submit a “pull request” (PR).

In the first few steps, we explain how to set up your git repository:

1. [Create an account](https://github.com/join) on GitHub if you do not already have one.

2. Fork the [project repository](): click on the ‘Fork’ button near the top of the page. 
This creates a copy of the code under your account on the GitHub user account. 
For more details on how to fork a repository see [this guide](https://help.github.com/articles/fork-a-repo/).

3. Clone your fork of the <PROJECT NAME> repo from your GitHub account to your local disk and add the base repository as a remote::

```bash
$ git clone git@github.com:<MY GITHUB HANDLE>/<PROJECT NAME>.git
$ cd <PROJECT NAME>
$ git remote add upstream https://github.com/<GITHUB HANDLE>/<PROJECT NAME>.git
```

4. Create a new branch to hold your development changes:

```bash
$ git checkout -b a-descriptive-name-for-my-changes
```

Do not work on the `master` branch.

5. Set up a development environment by running the following command in a virtual environment:

```bash
$ pip install -e ".[dev]"
```

You should now have a working installation of <PROJECT NAME>, and your git repository properly configured. 

The next steps now describe the process of modifying code and submitting a PR:

6. Develop the features on your branch.

As you work on the features, you should make sure that the test suite passes:

```bash
$ make test
```

<PROJECT NAME> relies on `black` and `isort` to format its source code consistently. After you make changes, format them with:

```bash
$ make style
```

<PROJECT NAME> uses `pylint` to check for coding mistakes. Quality control runs in CI, however you can also run the same checks with:

```bash
$ make quality
```

You can do the automatic style corrections and code verifications that can't be automated in one go:

```bash
$ make fixup
```

If you're modifying documents under `docs/source`, make sure to validate that they can still be built. 
This check also runs in CI. 
To run a local check make sure you have installed the documentation builder requirements, by running `pip install ."[doc]"` once from the root of this repository and then run:

```bash
$ make docs
```

Once you're happy with your changes, add changed files using git add and make a commit with git commit to record your changes locally:

```bash
$ git add modified_file.py
$ git commit
```

Please write a [good commit messages](https://chris.beams.io/posts/git-commit/).

It is a good idea to sync your copy of the code with the original repository regularly. This way you can quickly account for changes:

```bash
$ git fetch upstream
$ git rebase upstream/master
```

Push the changes to your account using:

```bash
$ git push -u origin a-descriptive-name-for-my-changes
```

7. Once you are satisfied (and the checklist below is happy too), go to the webpage of your fork on GitHub. 
Click on 'Pull request' to send your changes to the project maintainers for review.

8. It's ok if maintainers ask you for changes. 
It happens to core contributors too! So everyone can see the changes in the Pull request, work in your local branch and push the changes to your fork. 
They will automatically appear in the pull request.

It is often helpful to keep your local feature branch synchronized with the latest changes of the main scikit-learn repository:

```bash
$ git fetch upstream
$ git merge upstream/main
```

### Checklist

* The title of your pull request should be a summary of its contribution.

* If your pull request addresses an issue, please mention the issue number in the pull request description to make sure they are linked (and people consulting the issue know you are working on it).

* To indicate a work in progress please prefix the title with [WIP]. These are useful to avoid duplicated work, and to differentiate it from PRs ready to be merged.

* Make sure existing tests pass.

* Add high-coverage tests. No quality testing = no merge.

* All public methods must have informative docstrings.


## Style guide

For documentation strings, transformers follows the [google style](https://google.github.io/styleguide/pyguide.html). 
Check our [documentation writing guide]() for more information.

*This guide was heavily inspired by the awesome [scikit-learn guide to contributing](https://github.com/scikit-learn/scikit-learn/blob/master/CONTRIBUTING.md) and [HuggingFace Transformers](https://github.com/huggingface/transformers/blob/master/CONTRIBUTING.md#how-to-contribute-to-transformers)!*
