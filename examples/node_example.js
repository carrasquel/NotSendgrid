const sendGridMail = require('@sendgrid/mail');
sendGridMail.setApiKey("SG.unsecured_key");

function getMessage() {
  const body = 'This is a test email using SendGrid from Node.js';
  return {
    baseUrl: "http://localhost:3000",
    to: 'you@domain.com',
    from: 'verifiedemail@previousstep.com',
    subject: 'Test email with Node.js and SendGrid',
    text: body,
    html: `<strong>${body}</strong>`,
  };
}

async function sendEmail() {
  try {
    await sendGridMail.send(getMessage());
    console.log('Test email sent successfully');
  } catch (error) {
    console.error('Error sending test email');
    console.error(error);
    if (error.response) {
      console.error(error.response.body)
    }
  }
}

(async () => {
  console.log('Sending test email');
  await sendEmail();
})();