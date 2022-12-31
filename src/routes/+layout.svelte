<script>
  import '../app.scss';
  import NavBar from "./NavBar.svelte";
</script>

<div class="fixed top-0 w-full">
  <NavBar />
</div>

<div class="mt-20">
  <slot />
</div>
