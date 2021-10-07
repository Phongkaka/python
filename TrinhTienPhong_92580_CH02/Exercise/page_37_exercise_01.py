"""
Author: Trinh Tien Phong
Date: 25/09/2021
Program: page_37_exercise_02.py
Problem:
    1.  List four phases of the software development process, and explain what they
accomplish.
Solution:

Phase 1 – Development
This is where the application or software is ideated and created. Finding and fixing application security issues in
this early stage is far less costly than waiting until after an application has been deployed, so empowering developers
to create secure software from inception is critical.
To do this, create static assessments that are fully integrated within the environment where developers work, providing
them immediate feedback during creation. And if you add open source component analysis, developers will receive
automated alerts for known vulnerable components. Audited scan results, including line-of-code details and remediation
advice, help drive secure coding best practices.
------------------------------------------------------------------------------------------------------------------------
Phase 2 – Testing
Once an application is created, it should be further tested before it’s released in a live environment. Even if you
included security in your design, it may meet new challenges in a real-world situation.
A dynamic or mobile assessment of the running application in a QA, test or staging environment simulates the real-world
hacking techniques employed by potential hackers.
For web applications and web services, use dynamic assessments. These employ a combination of automated and manual
testing techniques to crawl the application attack surface and identify exploitable vulnerabilities before an
application release is deployed to production.
Similarly, mobile assessments employ a combination of automated and manual techniques to identify vulnerabilities across
all three tiers of the mobile ecosystem-client including the device, network, and backend services.
------------------------------------------------------------------------------------------------------------------------
Phase 3 – Deployment
With these tests completed, it’s time for deployment. But inevitably, not all vulnerabilities can be remediated for
every application before it goes live. Misconfigurations in production environments can introduce issues not present in
pre-production, and new zero-day vulnerabilities arise in between release cycles.
As soon as your application is live, repeat your tests to ensure everything is secure and working properly. But don’t
assume these one-and-done tests are the end of your security requirements.
------------------------------------------------------------------------------------------------------------------------
Phase 4 – Monitoring
Because technologies and cybersecurity threats constantly evolve, you’ll also want to ingrain security via monitoring.
A robust production monitoring regimen includes continuous dynamic scanning for vulnerabilities and risk profile
changes, discovery of rogue applications, and run time detection of security events in the application itself.
These tasks, plus the security testing required in the early stages of application development, are critical. But they
can be time-consuming and they require expertise to deploy correctly. That’s why many agencies leverage application
security services.

"""