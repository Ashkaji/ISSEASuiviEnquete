# Local Setup to contribute to the project

## **Prerequisites:**
- [Git installed on your machine](https://git-scm.com/downloads)

## **Steps:**

1. [Clone the repository](https://github.com/Ashkaji/ISSEASuiviEnquete.git) to your local directory:

```bash
git clone https://github.com/Ashkaji/ISSEASuiviEnquete.git
```

2. Create python virtual environment and run this commmand:

```
pip install -r requirements.txt
````



# Local Setup for ISSEASuiviEnquete Project with Docker

# **Prerequisites:**

- [Docker installed on your machine](https://docs.docker.com/get-started/)
- [Git installed on your machine](https://git-scm.com/downloads)

## **Steps:**

1. [Clone the repository](https://github.com/Ashkaji/ISSEASuiviEnquete.git):

```bash
git clone https://github.com/Ashkaji/ISSEASuiviEnquete.git
```
2. Build the Docker image:

```bash
docker build -t issea-enquete-django-app .
```
3. Run the container:

```bash
docker run -v "$(pwd):/issea-enquete-app" -p 8000:8000 issea-enquete-django-app
```
This maps the current directory to `/issea-enquete-app` inside the container and exposes port 8000.

4. Access the application:

Open http://localhost:8000 in your web browser.

5. Additionnal notes

- Use Git commands within the mounted directory as usual:
  - git status
  - git add .
  - git commit -m "Your commit message"
  - git push
- Changes made within the container will persist in the mounted directory and vice versa.
- Consider using docker-compose for managing multiple services and configurations.
- For production environments, explore alternative methods like Git-aware deployment tools or managing Git operations outside the container.

## Remember:

Adapt placeholders (repository URL, image name) to your project.
Install any additional dependencies required by your project.
Ensure proper permissions for the container user to access files within the mounted directory.

## Customization

- Modify the app.py file to change the behavior of the Python script.
- Add or update dependencies in the requirements.txt file as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE_URL) file for details.
