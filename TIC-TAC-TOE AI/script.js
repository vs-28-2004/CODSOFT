let board = ["", "", "", "", "", "", "", "", ""];
let player = "X";
let ai = "O";
let gameOver = false;
let gameStarted = false;

function updateStatus(message) {
    document.getElementById("status").innerText = message;
}

function startGame(first) {
    resetGame();
    gameStarted = true;
    if (first === "player") {
        updateStatus("Your Turn");
    } else {
        updateStatus("AI is thinking...");
        aiMove();
    }
}

function makeMove(index) {
    if (!gameStarted || gameOver || board[index] !== "") {
        return;
    }
    board[index] = player;
    document.getElementById(`cell${index}`).innerText = player;

    const pattern = getWinningPattern(player);

    if (pattern) {
        highlightWinner(pattern);
        updateStatus("You Win!");
        gameOver = true;
        return;
    }

    if (board.every(cell => cell !== "")) {
        updateStatus("It's a Tie!");
        gameOver = true;
        return;
    }

    updateStatus("AI is thinking...");
    aiMove();
}

function aiMove() {
    setTimeout(() => {

        let bestScore = -Infinity;
        let move;

        for (let i = 0; i < board.length; i++) {
            if (board[i] === "") {
                board[i] = ai;
                let score = minimax(board, 0, false);
                board[i] = "";
                if (score > bestScore) {
                    bestScore = score;
                    move = i;
                }
            }
        }
        if (move !== undefined) {
            board[move] = ai;
            document.getElementById(`cell${move}`).innerText = ai;
            const pattern = getWinningPattern(ai);

            if (pattern) {
                highlightWinner(pattern);
                updateStatus("AI Wins!");
                gameOver = true;
                return;
            }

            if (board.every(cell => cell !== "")) {
                updateStatus("It's a Tie!");
                gameOver = true;
                return;
            }
            updateStatus("Your Turn");
        }
    }, 600);
}

function minimax(board, depth, isMaximizing) {

    if (getWinningPattern(ai)) return 10 - depth;
    if (getWinningPattern(player)) return depth - 10;
    if (board.every(cell => cell !== "")) return 0;

    if (isMaximizing) {
        let bestScore = -Infinity;
        for (let i = 0; i < board.length; i++) {
            if (board[i] === "") {
                board[i] = ai;
                let score = minimax(board, depth + 1, false);
                board[i] = "";
                bestScore = Math.max(bestScore, score);
            }
        }
        return bestScore;
    } 
    else {
        let bestScore = Infinity;
        for (let i = 0; i < board.length; i++) {
            if (board[i] === "") {
                board[i] = player;
                let score = minimax(board, depth + 1, true);
                board[i] = "";
                bestScore = Math.min(bestScore, score);
            }
        }
        return bestScore;
    }
}

function getWinningPattern(symbol) {
    const winConditions = [
        [0, 1, 2],[3, 4, 5],
        [6, 7, 8],[0, 3, 6],
        [1, 4, 7],[2, 5, 8],
        [0, 4, 8],[2, 4, 6]
    ];

    for (let condition of winConditions) {
        if (
            board[condition[0]] === symbol &&
            board[condition[1]] === symbol &&
            board[condition[2]] === symbol
        ) {
            return condition;
        }
    }
    return null;
}

function highlightWinner(pattern) {

    pattern.forEach(index => {
        document
            .getElementById(`cell${index}`)
            .classList.add("winner");
    });
}

function resetGame() {

    board = ["", "", "", "", "", "", "", "", ""];
    gameOver = false;
    gameStarted = false;

    for (let i = 0; i < 9; i++) {
        document.getElementById(`cell${i}`).innerText = "";
        document.getElementById(`cell${i}`).classList.remove("winner");
    }

    updateStatus("Choose who starts first");
}

const cells = document.querySelectorAll(".cell");

cells.forEach((cell, index) => {
    cell.addEventListener("click", () => {
        makeMove(index);
    });
});

document
    .getElementById("restart")
    .addEventListener("click", resetGame);