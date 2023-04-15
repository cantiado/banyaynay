<script setup>
import Button from "./Button.vue";
</script>

<template>
  <div class="p-5 flex flex-col justify-between">
    <h2 class="text-2xl">Let's get started!</h2>
    <div class="justify-center">
      <h3 class="text-center text-xl">
        Click one of the options below to get started:
      </h3>
      <div class="flex flex-row gap-8 justify-center m-2 mt-5">
        <button
          type="button"
          class="rounded-md bg-pink border-black border-2 w-fit h-fit px-5 py-2"
        >
          Upload an image
        </button>
      </div>
    </div>
    <div></div>
  </div>
</template>
