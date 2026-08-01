# AI Usage Notes

## AI Tools Used

During the development of this project, I used ChatGPT as a learning assistant to understand FastAPI concepts, API design, debugging, and best practices.

---

## 1. Which parts were AI-generated vs. written by me?

AI assisted me with:

- Understanding FastAPI project structure.
- Creating API endpoint templates.
- Learning how to use Pydantic models.
- Implementing CRUD operations.
- Understanding JSON file storage.
- Learning filtering and summary logic.
- Explaining Python errors and debugging issues.
- Writing documentation guidance.

I personally:

- Implemented and organized the project.
- Understood and modified the generated code.
- Integrated all endpoints.
- Tested every API using Swagger UI.
- Verified JSON file storage.
- Fixed bugs related to data loading and saving.
- Added and tested update, delete, category filter, date filter, total calculation, and summary endpoints.

---

## 2. What did I validate, test, or change?

I manually verified that:

- Expenses were correctly stored in expenses.json.
- POST added new expenses successfully.
- GET returned all stored expenses.
- DELETE removed expenses permanently from the JSON file.
- PUT updated existing expenses.
- Category filtering returned correct results.
- Date filtering worked correctly.
- Total calculation matched stored expense values.
- Summary grouped expenses by category.
- Every endpoint was tested successfully using Swagger UI.

I also modified the code to ensure that every add, update, and delete operation saved changes back to the JSON file.

---

## 3. Which AI suggestions did I reject?

Some early AI suggestions stored data only in memory, which caused data loss after restarting the server.

I replaced that approach with JSON file persistence using load_expenses() and save_expenses(), ensuring that data remained available across server restarts.

I also simplified and adjusted parts of the code while learning the implementation to make it easier to understand and maintain.

---

## Learning Outcome

This project helped me understand:

- FastAPI fundamentals
- REST API development
- CRUD operations
- Request validation using Pydantic
- JSON file persistence
- API testing with Swagger UI
- Debugging and improving backend code

AI was used as a learning assistant throughout the project, while I verified, modified, tested, and understood the final implementation.