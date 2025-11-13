<?php

namespace ContainerIw3WgcT;

class TemplateVariablesProxy8884ada extends \PrestaShopBundle\Twig\Layout\TemplateVariables implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyProxyTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".parent::class."\0".'baseUrl' => [parent::class, 'baseUrl', null, 16],
        "\0".parent::class."\0".'controllerName' => [parent::class, 'controllerName', null, 16],
        "\0".parent::class."\0".'defaultTabLink' => [parent::class, 'defaultTabLink', null, 16],
        "\0".parent::class."\0".'installDirExists' => [parent::class, 'installDirExists', null, 16],
        "\0".parent::class."\0".'isDebugMode' => [parent::class, 'isDebugMode', null, 16],
        "\0".parent::class."\0".'isDisplayedWithTabs' => [parent::class, 'isDisplayedWithTabs', null, 16],
        "\0".parent::class."\0".'isFrontOfficeAccessibleForAdmins' => [parent::class, 'isFrontOfficeAccessibleForAdmins', null, 16],
        "\0".parent::class."\0".'isMaintenanceEnabled' => [parent::class, 'isMaintenanceEnabled', null, 16],
        "\0".parent::class."\0".'isMenuCollapsed' => [parent::class, 'isMenuCollapsed', null, 16],
        "\0".parent::class."\0".'isMultiShop' => [parent::class, 'isMultiShop', null, 16],
        "\0".parent::class."\0".'isRtlLanguage' => [parent::class, 'isRtlLanguage', null, 16],
        "\0".parent::class."\0".'isoUser' => [parent::class, 'isoUser', null, 16],
        "\0".parent::class."\0".'jsRouterMetadata' => [parent::class, 'jsRouterMetadata', null, 16],
        "\0".parent::class."\0".'version' => [parent::class, 'version', null, 16],
        'baseUrl' => [parent::class, 'baseUrl', null, 16],
        'controllerName' => [parent::class, 'controllerName', null, 16],
        'defaultTabLink' => [parent::class, 'defaultTabLink', null, 16],
        'installDirExists' => [parent::class, 'installDirExists', null, 16],
        'isDebugMode' => [parent::class, 'isDebugMode', null, 16],
        'isDisplayedWithTabs' => [parent::class, 'isDisplayedWithTabs', null, 16],
        'isFrontOfficeAccessibleForAdmins' => [parent::class, 'isFrontOfficeAccessibleForAdmins', null, 16],
        'isMaintenanceEnabled' => [parent::class, 'isMaintenanceEnabled', null, 16],
        'isMenuCollapsed' => [parent::class, 'isMenuCollapsed', null, 16],
        'isMultiShop' => [parent::class, 'isMultiShop', null, 16],
        'isRtlLanguage' => [parent::class, 'isRtlLanguage', null, 16],
        'isoUser' => [parent::class, 'isoUser', null, 16],
        'jsRouterMetadata' => [parent::class, 'jsRouterMetadata', null, 16],
        'version' => [parent::class, 'version', null, 16],
    ];

    public function getIsoUser(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getIsoUser(...\func_get_args());
        }

        return parent::getIsoUser(...\func_get_args());
    }

    public function isRtlLanguage(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isRtlLanguage(...\func_get_args());
        }

        return parent::isRtlLanguage(...\func_get_args());
    }

    public function getControllerName(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getControllerName(...\func_get_args());
        }

        return parent::getControllerName(...\func_get_args());
    }

    public function isMultiShop(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isMultiShop(...\func_get_args());
        }

        return parent::isMultiShop(...\func_get_args());
    }

    public function isMenuCollapsed(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isMenuCollapsed(...\func_get_args());
        }

        return parent::isMenuCollapsed(...\func_get_args());
    }

    public function getJsRouterMetadata(): array
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getJsRouterMetadata(...\func_get_args());
        }

        return parent::getJsRouterMetadata(...\func_get_args());
    }

    public function isDebugMode(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isDebugMode(...\func_get_args());
        }

        return parent::isDebugMode(...\func_get_args());
    }

    public function isInstallDirExists(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isInstallDirExists(...\func_get_args());
        }

        return parent::isInstallDirExists(...\func_get_args());
    }

    public function getVersion(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getVersion(...\func_get_args());
        }

        return parent::getVersion(...\func_get_args());
    }

    public function getDefaultTabLink(): ?string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getDefaultTabLink(...\func_get_args());
        }

        return parent::getDefaultTabLink(...\func_get_args());
    }

    public function isMaintenanceEnabled(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isMaintenanceEnabled(...\func_get_args());
        }

        return parent::isMaintenanceEnabled(...\func_get_args());
    }

    public function isFrontOfficeAccessibleForAdmins(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isFrontOfficeAccessibleForAdmins(...\func_get_args());
        }

        return parent::isFrontOfficeAccessibleForAdmins(...\func_get_args());
    }

    public function isDisplayedWithTabs(): bool
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->isDisplayedWithTabs(...\func_get_args());
        }

        return parent::isDisplayedWithTabs(...\func_get_args());
    }

    public function getBaseUrl(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getBaseUrl(...\func_get_args());
        }

        return parent::getBaseUrl(...\func_get_args());
    }
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('TemplateVariablesProxy8884ada', false)) {
    \class_alias(__NAMESPACE__.'\\TemplateVariablesProxy8884ada', 'TemplateVariablesProxy8884ada', false);
}
