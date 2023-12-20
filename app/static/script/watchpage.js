const episode_link = $(".episode-link")
episode_link.click(function() {
const this_ele = $(this)
const block_id = this_ele.data("block-id")
const block_ele = $(`.episode-block[data-block-id="${block_id}"]`)
const is_open = block_ele.data("open")


if(!is_open) {
$(`.episode-block`).removeClass("active")
$(`.episode-block`).data("open", false)
block_ele.addClass("active")
block_ele.data("open", true)
}
})
