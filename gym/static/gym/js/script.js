function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const button = document.querySelector(".menu-button");

    sidebar.classList.toggle("active");

    if (sidebar.classList.contains("active")) {
        button.classList.remove("closed");
    } else {
        button.classList.add("closed");
    }
}


