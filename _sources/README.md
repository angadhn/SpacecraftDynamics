# [Introduction to Spacecraft Dynamics book](http://www.angadhn.com/SpacecraftDynamics/)

## Introduction

Welcome to SpacecraftDynamics repository! 👋

This educational resource was built with 
[![Jupyter Book Badge](https://raw.githubusercontent.com/cooperrc/computational-mechanics/8789a7efef5b6178f6e4a1f05e69babdb1438fc4/images/badge.svg)](https://angadhn.github.io/ComputationalDynamics/kinematics/introduction.html)
to support the study of EMS515U: Introduction to Spacecraft Dynamics at the 
[School of Engineering and Material Sciences](https://www.sems.qmul.ac.uk/) within 
[Queen Mary, University of London](https://www.qmul.ac.uk/).

This project is a collection of modules aimed at undergraduate engineering students. Each module makes up separate lessons that are accompanied by computational problem-solving tutorials written as Jupyter notebooks (Python 🐍). This aims to develop the students' skills in 21<sup>st</sup> century computing by framing engineering problems as computational methods.

## Content

TBC.

## Notes

- This project is still under-development so 
  [contributions](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
  and 
  [suggestions](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) are welcome.

## Contributing

We welcome contributions from the community! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed guidelines on how to contribute to this project.

## How to create this Jupyter Book

### Creating an environment

1. `conda env create -f environment.yml`
2. `conda activate spacecraft-dynamics`

### Building a Jupyter Book

Run the following command in your terminal: `jb build .`.

If you would like to work with a clean build, you can empty the build folder by running `jb clean .`. If the jupyter execution is cached, this command will not delete the cached folder. To remove the build folder, you can run `jb clean --all .`.

### Publishing this Jupyter Book

Run `ghp-import -n -p -f _build/html`

## Instructor/Author:

- [Dr. Angadh Nanjangud](https://www.sems.qmul.ac.uk/staff/a.nanjangud)

## Student Contributors:
