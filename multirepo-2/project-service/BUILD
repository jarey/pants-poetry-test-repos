#poetry_requirements()
python_requirements(name="service_requires_dist", source="requirements.txt")
python_requirements(name="service_requires_test", source="requirements_dev.txt")

python_sources(
	name="service-lib",
	dependencies=[
	":project-service",
	"project_service:service-lib"
	]
)

python_distribution(
	name="service-dist",
	dependencies=[":service-lib",
	":service_requires_dist",
	"project-models:model-lib"],
	wheel=True,
	sdist=True,
	provides=setup_py(
		name="project_service",
		version="0.0.1",
		description="Project service.",
	),
)
