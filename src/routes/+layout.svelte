<script>
  import '../app.scss';
  import NavBar from "./NavBar.svelte";
</script>

<div class="sm:fixed top-0 w-full z-10">
  <NavBar />
</div>

<div class="sm:mt-20">
  <slot />
</div>
