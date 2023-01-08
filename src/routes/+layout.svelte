<script>
  export const prerender = true;
  export const ssr = true;
  export const csr = false;
  export const trailingSlash = true;

  import '../app.scss';
  import NavBar from "./NavBar.svelte";
</script>

<div class="sm:fixed top-0 w-full z-10">
  <NavBar />
</div>

<div class="sm:mt-20">
  <slot />
</div>
