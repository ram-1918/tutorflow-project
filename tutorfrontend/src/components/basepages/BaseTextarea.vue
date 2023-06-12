<template>
    <!-- <div class="container"> -->
        <div class="row">
            <div class="col-75">
                <slot name="question"></slot>
            </div>
        </div>
        <div class="row">
            <div class="col-75">
                <slot name="answer"></slot>
            </div>
            <div>
                <slot name="choosefile"></slot>
            </div>
        </div>
        <div class="row">
            <div class="col-75">
                <slot name="category"></slot>
            </div>
        </div>
        <div class="row">
            <div class="col-75" id="topic">
                <slot name="topic"></slot>
            </div>
        </div>
        <div class="row">
            <div class="col-75">
                <slot name="student"></slot>
            </div>
        </div>
        <div class="row">
            <div class="col-75">
                <slot name="links"></slot>
            </div>
        </div>
        <div class="row">
            <div class="col-75">
                <slot name="post"></slot>
            </div>
        </div>
    <!-- </div> -->
</template>

<style scoped>
.col-75 {
  float: left;
  width: 100%;
  margin-top: 2px;
}
.row::after {
  content: "";
  display: table;
  clear: both;
}

</style>

<script>
export default {
    props: ['mode']
};
</script>