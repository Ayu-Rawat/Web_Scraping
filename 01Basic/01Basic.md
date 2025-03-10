# Learning Scrapy for Web Scraping

I am learning Scrapy for web scraping and documenting my journey on GitHub.

---

## Lesson 1: Setting Up the Environment

Before diving into Scrapy, it's essential to set up the environment properly to ensure a smooth experience.

### Step 1: Install Python

Ensure that Python is installed on your system. You can verify this by running:
```sh
python --version
```
If Python is not installed, download and install it from the [official website](https://www.python.org/downloads/).

---

### Step 2: Install `pip`

`pip` is Python’s package manager. Check if it's installed by running:
```sh
pip --version
```
If `pip` is not installed, install it using:
```sh
python -m ensurepip --default-pip
```

---

### Step 3: Set Up a Virtual Environment

Using a virtual environment ensures that Scrapy and its dependencies remain isolated from other Python projects.

#### For Windows & Linux
1. Install `virtualenv`:
   ```sh
   pip install virtualenv
   ```
2. Create a virtual environment:
   ```sh
   virtualenv scrapy_env
   ```
3. Activate the virtual environment:
   - **Windows:**
     ```sh
     source ./scrapy_env/Scripts/activate
     ```
   - **Linux:**
     ```sh
     source scrapy_env/bin/activate
     ```

#### For macOS (Using `venv` Instead of `virtualenv`)
1. Create a virtual environment:
   ```sh
   python -m venv scrapy_env
   ```
2. Activate it:
   ```sh
   source scrapy_env/bin/activate
   ```

Once activated, you should see `(scrapy_env)` in your terminal, indicating that you're in the virtual environment.

#### Deactivating the Virtual Environment
When you're done working, it's good practice to deactivate the virtual environment to avoid conflicts:
```sh
deactivate
```
This works on all operating systems.

---

### Step 4: Install Scrapy

With the virtual environment activated, install Scrapy by running:
```sh
pip install scrapy
```

To confirm the installation, type:
```sh
scrapy
```
This should display Scrapy's command options, verifying a successful installation.

Now, you're all set to start web scraping with Scrapy!

---

Stay tuned for the next lesson, where we'll create our first Scrapy project.