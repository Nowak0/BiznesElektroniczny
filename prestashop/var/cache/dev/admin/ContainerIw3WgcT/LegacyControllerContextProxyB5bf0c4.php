<?php

namespace ContainerIw3WgcT;

class LegacyControllerContextProxyB5bf0c4 extends \PrestaShop\PrestaShop\Core\Context\LegacyControllerContext implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyProxyTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".'*'."\0".'adminFolderName' => [parent::class, 'adminFolderName', parent::class, 522],
        "\0".'*'."\0".'container' => [parent::class, 'container', parent::class, 522],
        "\0".'*'."\0".'employeeLanguageId' => [parent::class, 'employeeLanguageId', parent::class, 522],
        "\0".'*'."\0".'isLanguageRTL' => [parent::class, 'isLanguageRTL', parent::class, 522],
        "\0".'*'."\0".'languages' => [parent::class, 'languages', null, 8],
        "\0".'*'."\0".'physicalUri' => [parent::class, 'physicalUri', parent::class, 522],
        "\0".'*'."\0".'psVersion' => [parent::class, 'psVersion', parent::class, 522],
        "\0".'*'."\0".'request' => [parent::class, 'request', parent::class, 522],
        "\0".'*'."\0".'twig' => [parent::class, 'twig', parent::class, 522],
        'adminFolderName' => [parent::class, 'adminFolderName', parent::class, 522],
        'ajax' => [parent::class, 'ajax', null, 4],
        'className' => [parent::class, 'className', parent::class, 518],
        'confirmations' => [parent::class, 'confirmations', null, 4],
        'container' => [parent::class, 'container', parent::class, 522],
        'controller_name' => [parent::class, 'controller_name', parent::class, 518],
        'controller_type' => [parent::class, 'controller_type', parent::class, 518],
        'css_files' => [parent::class, 'css_files', null, 4],
        'currentIndex' => [parent::class, 'currentIndex', parent::class, 518],
        'employeeLanguageId' => [parent::class, 'employeeLanguageId', parent::class, 522],
        'errors' => [parent::class, 'errors', null, 4],
        'id' => [parent::class, 'id', parent::class, 518],
        'imageType' => [parent::class, 'imageType', null, 4],
        'informations' => [parent::class, 'informations', null, 4],
        'isLanguageRTL' => [parent::class, 'isLanguageRTL', parent::class, 522],
        'js_files' => [parent::class, 'js_files', null, 4],
        'languages' => [parent::class, 'languages', null, 8],
        'multishop_context' => [parent::class, 'multishop_context', parent::class, 518],
        'multishop_context_group' => [parent::class, 'multishop_context_group', null, 4],
        'override_folder' => [parent::class, 'override_folder', parent::class, 518],
        'page_header_toolbar_btn' => [parent::class, 'page_header_toolbar_btn', null, 4],
        'php_self' => [parent::class, 'php_self', parent::class, 518],
        'physicalUri' => [parent::class, 'physicalUri', parent::class, 522],
        'psVersion' => [parent::class, 'psVersion', parent::class, 522],
        'request' => [parent::class, 'request', parent::class, 522],
        'table' => [parent::class, 'table', parent::class, 518],
        'token' => [parent::class, 'token', parent::class, 518],
        'twig' => [parent::class, 'twig', parent::class, 522],
        'warnings' => [parent::class, 'warnings', null, 4],
    ];

    public function getTwig(): \Twig\Environment
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getTwig(...\func_get_args());
        }

        return parent::getTwig(...\func_get_args());
    }

    public function addCSS(array|string $css_uri, string $css_media_type = 'all', ?int $offset = null, bool $check_path = true): void
    {
        if (isset($this->lazyObjectState)) {
            ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->addCSS(...\func_get_args());
        } else {
            parent::addCSS(...\func_get_args());
        }
    }

    public function addJS(array|string $js_uri, bool $check_path = true): void
    {
        if (isset($this->lazyObjectState)) {
            ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->addJS(...\func_get_args());
        } else {
            parent::addJS(...\func_get_args());
        }
    }

    public function addJqueryUI(array|string $component, string $theme = 'base', bool $checkDependencies = true): void
    {
        if (isset($this->lazyObjectState)) {
            ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->addJqueryUI(...\func_get_args());
        } else {
            parent::addJqueryUI(...\func_get_args());
        }
    }

    public function addJqueryPlugin(array|string $name, ?string $folder = null, bool $css = true): void
    {
        if (isset($this->lazyObjectState)) {
            ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->addJqueryPlugin(...\func_get_args());
        } else {
            parent::addJqueryPlugin(...\func_get_args());
        }
    }

    public function getLanguages(): array
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getLanguages(...\func_get_args());
        }

        return parent::getLanguages(...\func_get_args());
    }

    public function getContainer(): \Symfony\Component\DependencyInjection\ContainerInterface
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getContainer(...\func_get_args());
        }

        return parent::getContainer(...\func_get_args());
    }

    public function loadLegacyMedia(): void
    {
        if (isset($this->lazyObjectState)) {
            ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->loadLegacyMedia(...\func_get_args());
        } else {
            parent::loadLegacyMedia(...\func_get_args());
        }
    }
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('LegacyControllerContextProxyB5bf0c4', false)) {
    \class_alias(__NAMESPACE__.'\\LegacyControllerContextProxyB5bf0c4', 'LegacyControllerContextProxyB5bf0c4', false);
}
