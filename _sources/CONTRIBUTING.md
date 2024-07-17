# Contributing to SpacecraftDynamics

Thank you for your interest in contributing to the SpacecraftDynamics repository! We appreciate your help in improving the project. Please follow the guidelines below to ensure a smooth collaboration.

## Getting Started

1. **Fork the Repository:**
   - Navigate to the [SpacecraftDynamics repository](https://github.com/angadhn/SpacecraftDynamics).
   - Click on the "Fork" button to create your own copy of the repository.

2. **Clone Your Fork:**
   - Clone your fork to your local machine using the following command:
     ```bash
     git clone https://github.com/your-username/SpacecraftDynamics.git
     ```
   - Replace `your-username` with your GitHub username.

3. **Add the Main Repository as a Remote:**
   - Navigate to your local repository:
     ```bash
     cd SpacecraftDynamics
     ```
   - Add the main repository as a remote named `upstream`:
     ```bash
     git remote add upstream https://github.com/angadhn/SpacecraftDynamics.git
     ```

## Making Changes

1. **Create a New Branch:**
   - Create a new branch for your changes:
     ```bash
     git checkout -b your-branch-name
     ```
   - Replace `your-branch-name` with a descriptive name for your branch.

2. **Make Your Changes:**
   - Make your changes to the code or documentation.
   - Commit your changes with a descriptive commit message:
     ```bash
     git add .
     git commit -m "Description of the changes made"
     ```

3. **Push to Your Fork:**
   - Push your changes to your fork on GitHub:
     ```bash
     git push origin your-branch-name
     ```

4. **Create a Pull Request:**
   - Navigate to your fork on GitHub.
   - Click on the "New pull request" button.
   - Ensure the base repository is `angadhn/SpacecraftDynamics` and the base branch is `main`.
   - Select your branch as the compare branch.
   - Add a title and description for your pull request, then click "Create pull request".

## Keeping Your Fork Updated

1. **Fetch and Merge Updates from Upstream:**
   - Fetch the latest changes from the main repository:
     ```bash
     git fetch upstream
     ```
   - Merge the changes into your local `main` branch:
     ```bash
     git checkout main
     git merge upstream/main
     ```
   - Push the updated `main` branch to your fork:
     ```bash
     git push origin main
     ```

2. **Update Your Working Branch:**
   - If you are working on a different branch, merge the latest `main` branch into your working branch:
     ```bash
     git checkout your-branch-name
     git merge main
     ```

## Branch Protection

The `main` branch is protected to ensure the stability and integrity of the codebase. The following rules are in place:
- **Require pull request reviews before merging:** All changes must be reviewed.
- **Require status checks to pass before merging:** All CI/CD checks must pass.
- **Require branch to be up-to-date before merging:** Branch must be up-to-date with `main`.
- **Prevent force pushes:** Force pushes are not allowed.
- **Prevent deletions:** The `main` branch cannot be deleted.

## Code Review and Merge

1. **Review:** Your pull request will be reviewed by other contributors. They may suggest changes or ask questions.
2. **Merge:** Once approved, your pull request will be merged into the `main` branch by a repository maintainer.

Thank you for your contributions! Your help is greatly appreciated.

If you have any questions or need further assistance, feel free to open an issue in the repository.

Happy coding!
