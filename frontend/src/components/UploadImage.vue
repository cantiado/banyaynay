<script setup>
import { ref } from "vue";
import Button from "./Button.vue";

const fileUploaded = ref(false);
const fileObjectURL = ref("");
const fileName = ref("No image chosen");

const emits = defineEmits(["submit"]);

function updateImageDisplay(event) {
  if (event.target.files.length) {
    fileUploaded.value = true;
    fileName.value = event.target.files[0].name;
    fileObjectURL.value = URL.createObjectURL(event.target.files[0]);
  } else {
    fileUploaded.value = false;
    fileName.value = "No image chosen";
    fileObjectURL.value = "";
  }
}

function submit() {
  const fileInput = document.getElementById("file-input");
  emits("submit", fileInput.files[0]);
}
</script>

<template>
  <div class="h-full flex flex-col justify-start gap-5 items-center">
    <h2 class="text-2xl mb-5 self-start">Image upload</h2>
    <div class="w-full">
      <label
        class="flex flex-row items-center border border-gray-900 rounded-lg bg-gray-50 cursor-pointer"
        for="file-input"
      >
        <span
          class="px-3 py-1 rounded-l-md bg-gray-900 hover:bg-gray-700 text-lg text-white"
          >Choose Image</span
        >
        <span class="px-3 py-1">{{ fileName }}</span>
      </label>
      <input
        @change="updateImageDisplay"
        class="hidden"
        type="file"
        id="file-input"
        name="file-input"
      />
      <p
        class="mt-1 text-sm text-gray-500 dark:text-gray-300"
        id="file_input_help"
      >
        PNG and JPEG only
      </p>
    </div>
    <div class="h-1/2 w-full flex flex-row justify-center items-center">
      <img class="h-full" v-if="fileObjectURL" :src="fileObjectURL" />
      <div
        v-else
        class="h-full w-full bg-white/20 border-4 border-dashed rounded-xl flex flex-row justify-center items-center text-4xl"
      >
        No image uploaded
      </div>
    </div>
    <button
      @click="submit"
      type="button"
      class="mt-5 rounded-md bg-pink border-black border-2 w-fit h-fit px-5 py-2"
      :class="{ 'bg-gray-400': !fileUploaded }"
      :disabled="!fileUploaded"
    >
      Submit
    </button>
  </div>
</template>
