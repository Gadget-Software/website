<script>
  let formStatus = "";
</script>

<form 
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

  <div 
    class="cf-turnstile" 
    data-sitekey="0x4AAAAAAB0wN7cDdLSLmIV5" 
    data-theme="light"
  ></div>

  <button type="submit">Send</button>
  <p>{formStatus}</p>
</form>
