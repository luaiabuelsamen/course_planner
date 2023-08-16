function highlightPrereqsAndCoreqs(courseCode, prereqs, coreqs) {
    const courseElement = document.getElementById(courseCode);
    if (courseElement) {
        const prereqCodes = prereqs.split(',');
        const coreqCodes = coreqs.split(',');
        courseElement.classList.add('highlight');

        prereqCodes.forEach(prereqCode => {
            const prereqElement = document.getElementById(prereqCode);
            if (prereqElement) {
                prereqElement.classList.add('highlight-prereq');
            }
        });

        coreqCodes.forEach(coreqCode => {
            const coreqElement = document.getElementById(coreqCode);
            if (coreqElement) {
                coreqElement.classList.add('highlight-coreq');
            }
        });
    }
}

function removeHighlights(courseCode, prereqs, coreqs) {
    const courseElement = document.getElementById(courseCode);
    if (courseElement) {
        const prereqCodes = prereqs.split(',');
        const coreqCodes = coreqs.split(',');

        courseElement.classList.remove('highlight');

        prereqCodes.forEach(prereqCode => {
        const prereqElement = document.getElementById(prereqCode);
        if (prereqElement) {
            prereqElement.classList.remove('highlight-prereq');
        }
        });

        coreqCodes.forEach(coreqCode => {
            const coreqElement = document.getElementById(coreqCode);
            if (coreqElement) {
                coreqElement.classList.remove('highlight-coreq');
            }
        });
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const sortableTable = new Sortable(document.querySelector('.sortable'), {
        animation: 150, // Animation speed in milliseconds
        handle: '.sortable-row', // The element to be used as the handle for dragging
        draggable: '.sortable-row', // The items to be draggable
    });
});
