var clip = new ClipboardJS('.btn');

clip.on("success", function() {
    document.body.insertAdjacentHTML('beforeend', '<div>copied!</div>');
});
clip.on("error", function() {
    document.body.insertAdjacentHTML('beforeend', '<div>that didn\'t work.</div>');
});