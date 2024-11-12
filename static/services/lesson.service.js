const getTree = (subject, chapter, lesson) =>
  new Promise(async (resolve, reject) => {
    try {
      const response = await baseAxios().get(documentGetTree, {
        params: {
          subject,
          chapter,
          lesson,
        },
      });

      return resolve(response.data);
    } catch (error) {}
  });
const getSpeak = (lesson) =>
  new Promise(async (resolve, reject) => {
    try {
      const response = await baseAxios().get(documentLessonAudio, {
        params: {
          lesson,
        },
      });
      return resolve(response.data);
    } catch (error) {}
  });
const getLesson = (lesson) =>
  new Promise(async (resolve, reject) => {
    try {
      const response = await baseAxios().get(documentLesson, {
        params: {
          lesson,
        },
      });

      return resolve(response.data);
    } catch (error) {}
  });
