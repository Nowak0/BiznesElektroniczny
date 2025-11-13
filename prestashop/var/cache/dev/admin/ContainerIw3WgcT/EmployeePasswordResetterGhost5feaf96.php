<?php

namespace ContainerIw3WgcT;

class EmployeePasswordResetterGhost5feaf96 extends \PrestaShopBundle\Security\Admin\EmployeePasswordResetter implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyGhostTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".parent::class."\0".'configuration' => [parent::class, 'configuration', null, 530],
        "\0".parent::class."\0".'cookieKey' => [parent::class, 'cookieKey', null, 530],
        "\0".parent::class."\0".'employeeRepository' => [parent::class, 'employeeRepository', null, 530],
        "\0".parent::class."\0".'entityManager' => [parent::class, 'entityManager', null, 530],
        "\0".parent::class."\0".'hashing' => [parent::class, 'hashing', null, 530],
        "\0".parent::class."\0".'router' => [parent::class, 'router', null, 530],
        "\0".parent::class."\0".'shopContext' => [parent::class, 'shopContext', null, 530],
        "\0".parent::class."\0".'translator' => [parent::class, 'translator', null, 530],
        'configuration' => [parent::class, 'configuration', null, 530],
        'cookieKey' => [parent::class, 'cookieKey', null, 530],
        'employeeRepository' => [parent::class, 'employeeRepository', null, 530],
        'entityManager' => [parent::class, 'entityManager', null, 530],
        'hashing' => [parent::class, 'hashing', null, 530],
        'router' => [parent::class, 'router', null, 530],
        'shopContext' => [parent::class, 'shopContext', null, 530],
        'translator' => [parent::class, 'translator', null, 530],
    ];
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('EmployeePasswordResetterGhost5feaf96', false)) {
    \class_alias(__NAMESPACE__.'\\EmployeePasswordResetterGhost5feaf96', 'EmployeePasswordResetterGhost5feaf96', false);
}
