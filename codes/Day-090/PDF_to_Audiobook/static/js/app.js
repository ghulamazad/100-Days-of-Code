$(function () {
  $(document).on("change", ":file", function () {
    let input = $(this);
    let filename = input.val().replace(/\\/g, "/").replace(/.*\//, "");
    let parentInput = $(this).parents(".input-group").find(":text");
    parentInput.val(filename);
  });
});
