INSERT INTO jobs (id, contact_email, password, company_name, job_title, job_description,
  location, salary_min, salary_max)
VALUES
  (111, 'tom@example.com', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f',
   'acme ltd', 'front end developer', 'developing the front end of the website', 'manchester', 30000, 60000)