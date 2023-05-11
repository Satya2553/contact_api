<!DOCTYPE html>
<html>
<body>
  <h1>Django Contact API</h1>
  
  <h2>Overview</h2>
  <p>This Django project demonstrates the implementation of a Contact API using Django REST Framework. It allows managing contact details such as names, companies, job titles, email addresses, phone numbers, birthdays, and notes.</p>
  
  <h2>Installation</h2>
  <p>Follow the steps below to set up and run the project:</p>
  <ol>
    <li>Clone the repository:</li>
  </ol>
  <pre><code>git clone https://github.com/Satya2553/contact_api</code></pre>
  <ol start="2">
    <li>Install the project dependencies:</li>
  </ol>
  <pre><code>pip install -r requirements.txt</code></pre>
  <ol start="3">
    <li>Navigate to the project directory:</li>
  </ol>
  <pre><code>cd contact_api</code></pre>
  <ol start="4">
    <li>Run the Django server:</li>
  </ol>
  <pre><code>python manage.py runserver</code></pre>
  
  <h2>API Endpoints</h2>
  <p>The following API endpoints are available:</p>
  <ul>
    <li><strong>GET /contact/</strong>: Retrieve a list of all contacts</li>
    <li><strong>POST /contact/</strong>: Create a new contact</li>
    <li><strong>GET /contact/{id}/</strong>: Retrieve details of a specific contact</li>
    <li><strong>PUT /contact/{id}/</strong>: Update details of a specific contact</li>
    <li><strong>DELETE /contact/{id}/</strong>: Delete a specific contact</li>
    <li><strong>SWAGGER API /swagger: To get the Swagger API documentation</strong></li>
  </ul>
  
  <h2>API Documentation</h2>
  <p>The API documentation is available using the Swagger UI:</p>
  <p>Swagger URL: <a href="/swagger">/swagger</a></p>
  <p>Visit the Swagger documentation to explore the API endpoints, make test requests, and understand the available request and response formats.</p>
  
</body>
</html>
