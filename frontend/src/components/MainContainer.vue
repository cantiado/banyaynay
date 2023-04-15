<script setup>
import { ref } from "vue";
import GetStarted from "./GetStarted.vue";
import ConfirmImage from "./ConfirmImage.vue";
import UploadImage from "./UploadImage.vue";
import LoadingView from "./LoadingView.vue";
import ClassifiedResult from "./ClassifiedResult.vue";

const index = ref(0);

function uploadImage(file) {
  console.log(file)
  index.value = 1;
}
</script>

<template>
  <div id="main-container" class="h-screen w-full bg-mellow-yellow p-10">
    <!-- Component views go here -->
    <!-- <GetStarted v-if="index == 0" /> -->
    <UploadImage v-if="index == 0" @submit="uploadImage" />
    <!-- <ConfirmImage v-if="index == 2" /> -->
    <LoadingView v-if="index == 1" />
    <ClassifiedResult v-if="index == 2" />
  </div>
</template>
