# EMS418U: [Computational Dynamics book](https://angadhn.github.io/ComputationalDynamics/kinematics/introduction.html)

## Introduction

Welcome to Computational Dynamics. 👋

This educational resource was built
with [![Jupyter Book Badge](https://raw.githubusercontent.com/cooperrc/computational-mechanics/8789a7efef5b6178f6e4a1f05e69babdb1438fc4/images/badge.svg)](https://angadhn.github.io/ComputationalDynamics/kinematics/introduction.html)
to support the study
of [EMS418U: Computational Dynamics](https://www.sems.qmul.ac.uk/ugadmissions/programmes/2021/yr1modules/#Computational%20mathematical%20modelling%202)
at
the [School of Eningeering and Material Sciences](https://www.sems.qmul.ac.uk/)
within
[Queen Mary, University of London](https://www.qmul.ac.uk/). 

This project is a collection of modules aimed
at undergraduate engineering students. Each module makes up separate lessons that
are accompanied by computational problem-solving tutorials
written as Jupyter notebooks (Python 🐍). This
aims to develop the students' skills in 21<sup>
st</sup> century computing by framing engineering
problems as computational methods.

## Content

- [Kinematics](https://angadhn.github.io/ComputationalDynamics/kinematics/introduction.html)
- [Inertia](https://angadhn.github.io/ComputationalDynamics/inertia/inertia-1.html)
- [Forces, Moments and Momenta](https://angadhn.github.io/ComputationalDynamics/forces-moments-momenta/forces-1.html)
- [Dynamics](https://angadhn.github.io/ComputationalDynamics/dynamics/dynamics-1.html)

## Notes

- This project is still under-development
  so [contributions](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
  and [suggestions](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) are welcome.

## How to create this Jupyter Book

### Creating an environment
1. `conda env create -f environment.yml`
2. `conda activate computational-mechanics-example`

### Building a Jupyter Book
Run the following command in your terminal: `jb build .`.
If you would like to work with a clean build, you can empty the build folder by running `jb clean .`. If the jupyter execution is cached, this command will not delete the cached folder. To remove the build folder, you can run `jb clean --all .`.

### Publishing this Jupyter Book

Run `ghp-import -n -p -f _build/html`

## Active Contributors:

- [Dr. Angadh Nanjangud](https://www.sems.qmul.ac.uk/staff/a.nanjangud)
- Simone Asci
- Mughees Asif




