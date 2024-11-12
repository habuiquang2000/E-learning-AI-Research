const getCategories = () =>
  new Promise(async (resolve, reject) => {
    try {
      const response = await baseAxios().get(documentCategoriesEndpoint, {});
      return resolve(response.data);
    } catch (error) {
      return reject(error);
    }
  });
const getSubjects = (category) =>
  new Promise(async (resolve, reject) => {
    try {
      const response = await baseAxios().get(documentSubjectsEndpoint, {
        params: {
          category,
        },
      });
      return resolve(response.data);
    } catch (error) {
      return reject(error);
    }
  });
const getChapters = (subject) =>
  new Promise(async (resolve, reject) => {
    try {
      const response = await baseAxios().get(documentChaptersEndpoint, {
        params: {
          subject,
        },
      });
      return resolve(response.data);
    } catch (error) {
      return reject(error);
    }
  });

const postDocumentFile = (formData) =>
  new Promise(async (resolve, reject) => {
    try {
      const response = await baseAxios().post(
        documentFromWordEndpoint,
        formData,
        {}
      );

      return resolve(response.data);
    } catch (error) {
      return reject(error);
    }
  });
const postDocumentContent = (content) =>
  new Promise(async (resolve, reject) => {
    try {
      const response = await baseAxios().post(documentPostContentEndpoint, {
        data: content,
      });

      return resolve(response.data);
    } catch (error) {
      return reject(error);
    }
  });
