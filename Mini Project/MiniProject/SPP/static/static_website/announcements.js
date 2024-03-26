document.addEventListener('DOMContentLoaded', function() {
    fetch('/get_latest_announcements/')
        .then(response => response.json())
        .then(data => {
            const announcements = data.announcements;
            const announcementsList = document.createElement('ul'); // Create unordered list
            announcementsList.classList.add('announcement-list'); // Add class for styling

            announcements.forEach(announcement => {
                // Create list item for each announcement
                const listItem = document.createElement('li');
                listItem.innerHTML = `
                    <h3>${announcement.title}</h3>
                    <p>${announcement.content}</p>
                `;
                announcementsList.appendChild(listItem); // Append list item to unordered list
            });

            const announcementsSection = document.querySelector('.announcements');
            announcementsSection.innerHTML = ''; // Clear previous content
            announcementsSection.appendChild(announcementsList); // Append unordered list to announcements section
        })
        .catch(error => console.error('Error fetching announcements:', error));
});
