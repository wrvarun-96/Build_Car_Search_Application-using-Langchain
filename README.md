# LangChain Car Brand Information Chain

This repository demonstrates how to use the LangChain library to create a multi-step workflow for retrieving and processing information about car brands using OpenAI's language model. Custom number of prompts  and the number of chains can be modified based on your choice.

## Overview

The project sets up three sequential chains of operations using prompt templates and the OpenAI language model. The first chain retrieves information about a car brand, the second chain provides more detailed information about a specific car model obtained from the first chain's output, and the third chain lists 5 models from the car brand obtained from the first chain's output.

## Installation

To run this project, you need to have Python installed along with the necessary libraries. You can install the required libraries using pip:
