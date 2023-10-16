python_requirements(name="model_requires_dist", source="requirements.txt")
python_requirements(name="model_requires_test", source="requirements_dev.txt")

python_sources(
	name="model-lib",
	dependencies=[
	":project-models", 
	"project_models:model-lib"
	]
)

python_distribution(
	name="model-dist",
	dependencies=[":model-lib",":model_requires_dist"],
	wheel=True,
	sdist=True,
	provides=setup_py(
		name="project_models",
		version="0.0.1",
		description="Project model.",
	),
)
