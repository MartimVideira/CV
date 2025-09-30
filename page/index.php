<?php
    $data = ["prefered_name" => "Martim Videira"];

    require 'vendor/autoload.php';
    use Symfony\Component\Yaml\Yaml;

    $yaml = file_get_contents("./../experience.yaml");

    $data = Yaml::parse($yaml);
    $parseDown = new Parsedown();

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> <?php echo $data["prefered_name"] ?>'s CV </title>   

</head>
<body>
    <h1> <?php echo $data["prefered_name"] ?> </h1>
    <nav>
        <ul>
            <li><a href="<?= $data["github"]["link"]?>"><?= $data["github"]["display"]?></a></li>
            <li><a href="<?= $data["linkedin"]["link"]?>"><?= $data["linkedin"]["display"]?></a></li>
            <li><a href="mailto:<?= $data["email"]?>"><?= $data["email"]?></a></li>
        </ul>
    </nav>
    <section id="education" >
        <h2>Education</h2>
        <p>Degree in <?= $data["education"]["degree"] ?> from the <?= $data["education"]["university"] ?> <?= $data["education"]["from"]["begin"] ?> to <?= $data["education"]["from"]["end"] ?> </p>
    </section>
    <section id="experience" >
        <h2>Experience</h2>
        <section id="experience-container">
        <?php  foreach ($data["experience"] as $experience) { ?>
            <article class="experience">
            <h3> <?= $experience["position"]?> </h3>
            <div> <?= $parseDown->text($experience["description"])?> </div>
        <?php } ?>
        </section>
    </section>
    <section id="projects">
        <h2>Projects</h2>
        <section id="projects-container">
        <?php  foreach ($data["projects"] as $project) { ?>
            <article class="project">
            <h3> <?= $project["name"]?> </h3>
            <div> <?= $parseDown->text($project["description"])?> </div>
            <ul>
            <?php  foreach ($project["technologies"] as $technology) { ?>
                <li><?= $technology ?>  </li>
            <?php } ?>
            </ul>
        <?php } ?>
    </section>
    </section>
    <section id="programming-languages">
        <h2>Programming Languages</h2>
        <ul>
        <?php  foreach ($data["programming_languages"] as $language) { ?>
            <li> <?= $language ?> </li>
        <?php } ?>
        </ul>
    </section>
    <section id="technologies">
        <h2>Technologies</h2>
        <ul>
        <?php  foreach ($data["technologies"] as $technology) { ?>
            <li> <?= $technology?> </li>
        <?php } ?>
        </ul>
    </section>
    <section id="languages">
        <h2>Languages</h2>
        <ul>
        <?php  foreach ($data["languages"] as $language) { ?>
            <li> <?= $language["l"]?> </li>
            <li> <?= $language["level"]?> </li>
        <?php } ?>
        </ul>
    </section>
</body>
</html>