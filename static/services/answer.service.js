const postAnswerTrain = (answers) =>
  new Promise(async (resolve, reject) => {
    try {
      const response = await baseAxios().post(answerTrainEndpoint, {
        data: answers,
      });

      return resolve(response.data);
    } catch (error) {
      return reject(error);
    }
  });

//   data: {
//     isRoot: true,
//     slug: data.slug,
//     children: [
//       {
//         order: 1,
//         title: "WorkLoad",
//         slug: "123",
//         isExpand: true,
//         children: [
//           { order: 1.1, slug: "1.1", title: "DME Report" },
//           { order: 1.2, slug: "1.2", title: "CAMB Report" },
//           { order: 1.3, slug: "1.3", title: "LMAB Report" },
//           { order: 1.4, slug: "1.4", title: "DMF Notification" },
//         ],
//       },
//       {
//         order: 2,
//         title: "Performance",
//         slug: "456",
//         isExpand: true,
//         children: [
//           { order: 2.1, slug: "2.1", title: "LME Forecast Report" },
//           { order: 2.2, slug: "2.2", title: "Calendar" },
//           { order: 2.3, slug: "2.3", title: "Efficiency" },
//           { order: 2.4, slug: "2.4", title: "Process Age" },
//         ],
//       },
//     ],
//   },
// });
// try {
//   const response = await baseAxios().get("/", {
//     params: {
//       // _limit: 5,
//       // page: subjectId,
//       search: `{"s":${subjectId}}`,
//     },
//     timeout: 5000,
//   });

// return response.data;

// } catch (error) {
//   return {
//     status: `${error.status}`,
//     message: error.message,
//     data: error.code,
//   };
// }

// const updateTodoList = todoItems => {
//   const todoList = document.querySelector('ul');

//   if (Array.isArray(todoItems) && todoItems.length > 0) {
//     todoItems.map(todoItem => {
//       todoList.appendChild(createTodoElement(todoItem));
//     });
//   } else if (todoItems) {
//     todoList.appendChild(createTodoElement(todoItems));
//   }
// };
