# 0x19 postmortem
Report: Postmortem Analysis of Docker Conrtainer Outage
Issue Summary
* Duration of Outage: The Docker container outage occurred on Aug 28th, 2023, starting at 3:00 AM UTC and ending at 5:00 AM UTC.
* Impact: The outage affected the service mapped to port 8080 on the Docker container. 100% of users experienced a complete unavailability of the service during this time.
* Root Cause: A misconfiguration of the Apache web server within the Docker container prevented it from serving the intended web page.

Timeline
* 3:05 AM - Tested access to website directly which confirmed outage.
* 3:10 AM - Investigation began immediately, with a focus on the Docker container and its configuration.
* 4:15 AM - The root cause of the issue was identified as a misconfiguration in the Apache web server within the Docker container.
* 4:30 AM - An update of server was performed.
* 4:35 AM - A basic web page with the text "Hello Holberton" was created and placed in the appropriate directory.
* 4:45 AM - Finally, the Apache service was restarted.
* 5:00 AM - Confirmed full restoration of website functionality.

Root Cause and Resolution
* Root Cause: The root cause of the issue was a misconfiguration in the Apache web server settings within the Docker container.
* Resolution: The issue was resolved by updating and reinstalling Apache on the container and ensuring that the correct web page was served.

Corrective and Preventative Measures
* Improvements and Fixes: Regularly review and document container configurations to prevent misconfigurations. Implement automated monitoring and alerting systems to detect service unavailability. Document and follow best practices for containerized applications to prevent similar issues.
* Specific Tasks: Set up automated monitoring to alert on service unavailability and misconfigurations. Establish a clear documentation process for containerized applications to ensure proper configuration and maintence.
