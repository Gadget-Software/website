<script>
  import Column from "./Column.svelte";
  import Logo from "./Logo.svelte";
</script>

<div class="w-full h-20 bg-white">
  <Column>
    <div class="flex flex-row justify-between">
      <div>
        <Logo />
      </div>
      <div class="flex flex-row justify-between">
        <ul>
          <li>Our Services</li>
          <li>About Us</li>
        </ul>
        <button>
          Book a consultation
        </button>
      </div>
    </div>
  </Column>
</div>
