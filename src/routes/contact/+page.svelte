<script>
  let formStatus = "";
</script>

<form 
  class="contact-form"
  action="https://api.web3forms.com/submit" 
  method="POST" 
  on:submit={() => formStatus = 'Submitting...'}
>
  <input type="hidden" name="access_key" value="7e754091-28ab-42ae-a916-8caa835f4549" />
  <input type="hidden" name="subject" value="New Contact Message from Website" />

  <label>
    Name:
    <input type="text" name="name" required />
  </label>
  <label>
    Email:
    <input type="email" name="email" required />
  </label>
  <label>
    Message:
    <textarea name="message" required></textarea>
  </label>

  <button type="submit">Send</button>
  <p>{formStatus}</p>
</form>

<style>
.contact-form {
  max-width: 420px;
  margin: 3em auto;
  padding: 2em 2.5em 2.5em 2.5em;
  border-radius: 12px;
  box-shadow: 0 2px 16px 0 rgba(0,0,0,0.08);
  background: #fff;
  display: flex;
  flex-direction: column;
  gap: 1.2em;
}

.contact-form h2 {
  text-align: center;
  margin-bottom: .5em;
  color: #2a2e34;
  font-size: 1.4em;
  font-weight: 600;
}

.contact-form label {
  display: flex;
  flex-direction: column;
  font-weight: 500;
  gap: 0.4em;
  color: #23272f;
}

.contact-form input[type="text"],
.contact-form input[type="email"],
.contact-form textarea {
  padding: 0.7em;
  border: 1px solid #d0d4da;
  border-radius: 6px;
  font-size: 1em;
  transition: border-color .2s;
  background: #fafbfc;
}

.contact-form input:focus,
.contact-form textarea:focus {
  outline: none;
  border-color: #6a8cff;
  background: #f0f6ff;
}

.contact-form button {
  margin-top: 0.8em;
  background: #6a8cff;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 0.9em 1.2em;
  font-size: 1em;
  font-weight: 600;
  cursor: pointer;
  transition: background .17s;
}

.contact-form button:hover {
  background: #5273e0;
}

.form-status {
  text-align: center;
  color: #6a8cff;
  font-size: .95em;
  margin-top: .5em;
}

.cf-turnstile {
  margin: 0.5em 0 0.5em 0;
  align-self: center;
}
</style>

<Footer />
