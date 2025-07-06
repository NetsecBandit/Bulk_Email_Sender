import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# Email configuration
sender_email = "razaranasaim@gmail.com"  # Replace with your email
sender_password = "fzfc kaxe crew zqov"   # Replace with the 16-digit App Password
smtp_server = "smtp.gmail.com"         # SMTP server for Gmail
smtp_port = 587                        # SMTP port for TLS

# List of recipient email addresses
recipients = ["careers@digital-dividend.com", "jobs@appsnation.co", "amna.ahsan@contour-software.com", "hr@devsort.net", "careers@brainxtech.com", "zeeshan.hr0012@consoledot.com", "hr@bizzclan.com", "basit.ali@alfatah.com.pk", "careers@rendream.work"]  # Replace with actual HR email addresses

# Path to the PDF file to attach
pdf_file_path = "/media/netsec/New Volume1/resume.pdf"  # Replace with the actual path to your PDF file

# Email content
subject = "Inquiry About Internship Opportunities"
body = """Dear HR Team,

I hope you will be having a great day. My name is Rana Saim Raza, and I am currently an undergraduate student pursuing a degree in Software Engineering. I am deeply passionate about cybersecurity and am eager to apply my skills and enthusiasm in a professional setting.

I am writing to inquire about the availability of internship opportunities within your organization. If such opportunities are available, I would be thrilled to contribute to your team. I am highly motivated, quick to learn, and committed to gaining hands-on experience in the field of cybersecurity.

Please let me know if there are any open internship positions or upcoming opportunities. Attached is my resume.

Thank you for your time and consideration. I look forward to hearing from you.

Best regards,  
Rana Saim Raza
"""

# Function to send email with PDF attachment
def send_email(sender, password, recipients, subject, body, pdf_path):
    try:
        # Verify that the PDF file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found at: {pdf_path}")

        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS
        server.login(sender, password)

        # Send email to each recipient
        for recipient in recipients:
            # Create a new MIME object for each recipient
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Attach the PDF file
            with open(pdf_path, "rb") as f:
                pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
                pdf_attachment.add_header(
                    'Content-Disposition', 'attachment', filename=os.path.basename(pdf_path)
                )
                msg.attach(pdf_attachment)

            # Send the email
            server.sendmail(sender, recipient, msg.as_string())
            print(f"Email sent to {recipient}")

        # Close the connection
        server.quit()
        print("All emails sent successfully!")

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Execute the email sending function
if __name__ == "__main__":
    send_email(sender_email, sender_password, recipients, subject, body, pdf_file_path)