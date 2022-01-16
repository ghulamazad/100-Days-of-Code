const getCard = (name, description, link) => {
  var newNode = document.createElement("div");
  newNode.className = "col-xl-3 col-sm-6 col-12";
  newNode.innerHTML = `<div class="card">
                                <div class="card-body">
                                <h5 class="card-title">${name}</h5>
                                <p class="card-text">
                                ${description}
                                </p>
                                <a href="${link}" class="btn btn-primary">Source Code</a>
                                </div>
                            </div>`;
  return newNode;
};

const displayProjects = (projects) => {
  const cardWrapper = document.getElementById("card-wrapper");
  projects.forEach((project) => {
    cardWrapper.appendChild(
      getCard(project.name, project.description, project.link)
    );
  });
};

// Fetch data from json file
const projectJsonFile =
  "https://raw.githubusercontent.com/GhulamAzad/100-Days-of-Code/master/docs/data/projects.json";

fetch(projectJsonFile)
  .then((data) => data.json())
  .then((data) => {
    displayProjects(data.projects);
  });
