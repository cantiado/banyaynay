<script setup>
import { ref } from "vue";
import GetStarted from "./GetStarted.vue";
import ConfirmImage from "./ConfirmImage.vue";
import UploadImage from "./UploadImage.vue";
import LoadingView from "./LoadingView.vue";
import ClassifiedResult from "./ClassifiedResult.vue";

const url = "http://127.0.0.1:5000/upload";

const index = ref(0);
const imageUrl = ref("");

function reset() {
  index.value = 0;
  imageUrl.value = 0;
}

function uploadImage(file) {
  index.value = 1;
  const form = new FormData();
  form.append("image", file);
  fetch(url, {
    method: "POST",
    body: form,
  })
    .then((res) => res.json())
    .then((res) => {
      console.log(res);
      imageUrl.value = url + "/" + res.fname;
    })
    .catch((err) => {
      console.log(err);
      imageUrl.value = "";
    })
    .finally(() => {
      index.value = 2;
    });
}
</script>

<template>
  <div id="banyaynay-ify" class="h-screen w-full bg-mellow-yellow p-10">
    <!-- Component views go here -->
    <!-- <GetStarted v-if="index == 0" /> -->
    <UploadImage v-if="index == 0" @submit="uploadImage" />
    <!-- <ConfirmImage v-if="index == 2" /> -->
    <LoadingView v-if="index == 1" />
    <ClassifiedResult v-if="index == 2" :imgSrc="imageUrl" @reset="reset" />
  </div>
</template>
