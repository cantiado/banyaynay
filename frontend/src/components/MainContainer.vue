<script setup>
import GetStarted from './GetStarted.vue';
import ConfirmImage from './ConfirmImage.vue';
import UploadImage from './UploadImage.vue';
import LoadingView from './LoadingView.vue';
import ClassifiedResult from './ClassifiedResult.vue';
</script>

<template>
    <div id="main-container" class="h-screen w-screen grid grid-cols-1 fliex items-stretch bg-mellow-yellow p-5 pt-10">
        <!-- Component views go here -->
        <!-- <GetStarted /> -->
        <!-- <UploadImage /> -->
        <!-- <ConfirmImage /> -->
        <!-- <LoadingView /> -->
        <ClassifiedResult />
    </div>
</template>