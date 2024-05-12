// Example leaderboard data (replace with actual data)
const leaderboardData = [
    { rank: 1, participant: 'User1', score: 95 },
    { rank: 2, participant: 'User2', score: 90 },
    { rank: 3, participant: 'User3', score: 85 },
    { rank: 4, participant: 'User4', score: 80 },
    { rank: 5, participant: 'User5', score: 75 },
];

// Function to populate the leaderboard
function populateLeaderboard(data) {
    const leaderboard = document.getElementById("leaderboard");
    const tbody = leaderboard.getElementsByTagName("tbody")[0];

    data.forEach((entry) => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${entry.rank}</td>
            <td>${entry.participant}</td>
            <td>${entry.score}</td>
        `;
        tbody.appendChild(row);
    });
}

// Populate the leaderboard on page load
window.onload = () => {
    populateLeaderboard(leaderboardData);
};
