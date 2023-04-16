<script setup>
import { ref } from "vue";
import ImageContainer from "./ImageContainer.vue";
import Button from "./Button.vue";
import {
  TransitionRoot,
  TransitionChild,
  Dialog,
  DialogPanel,
  DialogTitle,
} from "@headlessui/vue";

const props = defineProps({
  imgSrc: {
    type: String,
    required: true,
  },
});

const isOpen = ref(false);
function openModal() {
  isOpen.value = true;
}
function closeModal() {
  isOpen.value = false;
}

const downloaded = ref(false);
function confirmDownloaded() {
  downloaded.value = true;
}

const emits = defineEmits(["reset"]);
function newImage() {
  if (downloaded.value || props["imgSrc"] == "") {
    emits("reset");
  } else {
    openModal();
  }
}
</script>

<template>
  <div class="p-5 flex flex-col justify-between">
    <div>
      <h2 class="text-2xl">Your picture has been banyaynay-ified!</h2>
    </div>
    <div class="justify-center">
      <div class="flex justify-center">
        <!-- <ImageContainer path="../assets/b1.jpg" /> -->
        <img v-if="imgSrc" :src="imgSrc" />
        <div
          v-else
          class="h-full w-full bg-white/20 border-4 border-dashed rounded-xl flex flex-row justify-center items-center text-4xl"
        >
          Oops! It seems an error occured somewhere. Better luck next time ;P
        </div>
      </div>
    </div>
    <div class="flex justify-between">
      <button
        @click="newImage"
        type="button"
        class="mt-5 rounded-md bg-pink border-black border-2 w-fit h-fit px-5 py-2"
      >
        New image
      </button>
      <a :href="imgSrc" download>
        <button
          @click="confirmDownloaded"
          type="button"
          class="mt-5 rounded-md bg-pink border-black border-2 w-fit h-fit px-5 py-2"
        >
          Download
        </button>
      </a>
    </div>
  </div>
  <TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="closeModal" class="relative z-10">
      <TransitionChild
        as="template"
        enter="duration-300 ease-out"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="duration-200 ease-in"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div class="fixed inset-0 bg-black bg-opacity-25" />
      </TransitionChild>

      <div class="fixed inset-0 overflow-y-auto">
        <div
          class="flex min-h-full items-center justify-center p-4 text-center"
        >
          <TransitionChild
            as="template"
            enter="duration-300 ease-out"
            enter-from="opacity-0 scale-95"
            enter-to="opacity-100 scale-100"
            leave="duration-200 ease-in"
            leave-from="opacity-100 scale-100"
            leave-to="opacity-0 scale-95"
          >
            <DialogPanel
              class="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all"
            >
              <DialogTitle
                as="h3"
                class="text-lg font-medium leading-6 text-gray-900"
              >
                Are you sure?
              </DialogTitle>
              <div class="mt-2">
                <p class="text-sm text-gray-500">
                  It seems you have not downloaded your result. If you want to
                  continue with a new image, confirm your decision below.
                </p>
              </div>

              <div class="mt-4">
                <button
                  type="button"
                  class="inline-flex justify-center rounded-md border border-transparent bg-blue-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                  @click="emits('reset')"
                >
                  Confirm
                </button>
                <button
                  type="button"
                  class="ml-3 inline-flex justify-center rounded-md border border-transparent px-4 py-2 text-sm font-medium text-gray-900 hover:bg-gray-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-500 focus-visible:ring-offset-2"
                  @click="closeModal"
                >
                  Cancel
                </button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>
